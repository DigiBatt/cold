
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OverpotentialModule import Overpotential







class OhmicOverpotential(Overpotential):
    """
    Class representing the `OhmicOverpotential` entity, which inherits from:
    - Overpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_03a6ce70_5085_4683_bb4e_fc3c18f7143a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OhmicOverpotential'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OhmicOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_03a6ce70_5085_4683_bb4e_fc3c18f7143a',
    
    class_name='OhmicOverpotential',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_03a6ce70_5085_4683_bb4e_fc3c18f7143a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OhmicOverpotential',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
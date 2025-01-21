
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalPhenomenonModule import PhysicalPhenomenon







class Neutralisation(PhysicalPhenomenon):
    """
    Class representing the `Neutralisation` entity, which inherits from:
    - PhysicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0471ec77_91bc_4a78_be31_b6af613e5966'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Neutralisation'`
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
    obj = Neutralisation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0471ec77_91bc_4a78_be31_b6af613e5966',
    
    class_name='Neutralisation',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0471ec77_91bc_4a78_be31_b6af613e5966',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Neutralisation',
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
    

    
    

    

    
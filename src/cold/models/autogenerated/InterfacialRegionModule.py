
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonTemporalRoleModule import NonTemporalRole







class InterfacialRegion(NonTemporalRole):
    """
    Class representing the `InterfacialRegion` entity, which inherits from:
    - NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f78e3c87_01c6_4cc2_b047_30322262e22d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InterfacialRegion'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InterfacialRegion(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f78e3c87_01c6_4cc2_b047_30322262e22d',
    
    class_name='InterfacialRegion',
    
    elucidation="example_value",
    
    figure="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f78e3c87_01c6_4cc2_b047_30322262e22d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InterfacialRegion',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    figure: Optional[str] = Field(
        None,
        alias="figure"
    )
    

    
    

    

    
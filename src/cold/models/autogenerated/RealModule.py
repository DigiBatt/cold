
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberModule import Number







class Real(Number):
    """
    Class representing the `Real` entity, which inherits from:
    - Number

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_18d180e4_5e3e_42f7_820c_e08951223486'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Real'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasNumericalValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Real(
    
    class_iri='https://w3id.org/emmo#EMMO_18d180e4_5e3e_42f7_820c_e08951223486',
    
    class_name='Real',
    
    elucidation="example_value",
    
    hasNumericalValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_18d180e4_5e3e_42f7_820c_e08951223486',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Real',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasNumericalValue: Optional[str] = Field(
        None,
        alias="hasNumericalValue"
    )
    

    
    

    

    
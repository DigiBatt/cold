
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CaseModule import Case







class SwagelokCase(Case):
    """
    Class representing the `SwagelokCase` entity, which inherits from:
    - Case

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd1b7943_42ce_46bd_8588_1c3161268270'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SwagelokCase'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SwagelokCase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd1b7943_42ce_46bd_8588_1c3161268270',
    
    class_name='SwagelokCase',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_cd1b7943_42ce_46bd_8588_1c3161268270',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SwagelokCase',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
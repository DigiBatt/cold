
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ElectrochemicalControlQuantity(ElectrochemicalQuantity):
    """
    Class representing the `ElectrochemicalControlQuantity` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5047d29_4e68_43ee_8355_3e8f05dc70a5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalControlQuantity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalControlQuantity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5047d29_4e68_43ee_8355_3e8f05dc70a5',
    
    class_name='ElectrochemicalControlQuantity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c5047d29_4e68_43ee_8355_3e8f05dc70a5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalControlQuantity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
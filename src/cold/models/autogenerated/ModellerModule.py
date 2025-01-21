
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EstimatorModule import Estimator







class Modeller(Estimator):
    """
    Class representing the `Modeller` entity, which inherits from:
    - Estimator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f94e509a_be29_4365_a4cd_70165e47e232'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Modeller'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Modeller(
    
    class_iri='https://w3id.org/emmo#EMMO_f94e509a_be29_4365_a4cd_70165e47e232',
    
    class_name='Modeller',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f94e509a_be29_4365_a4cd_70165e47e232',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Modeller',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    
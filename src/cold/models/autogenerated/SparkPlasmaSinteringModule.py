
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class SparkPlasmaSintering(Sintering):
    """
    Class representing the `SparkPlasmaSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f0644f69_7337_4385_9d4a_4401b7bf3302'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SparkPlasmaSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SparkPlasmaSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_f0644f69_7337_4385_9d4a_4401b7bf3302',
    
    class_name='SparkPlasmaSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f0644f69_7337_4385_9d4a_4401b7bf3302',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SparkPlasmaSintering',
        alias="class_name"
    )
    

    
    

    

    
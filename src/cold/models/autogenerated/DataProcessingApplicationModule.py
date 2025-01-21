
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ApplicationProgramModule import ApplicationProgram







class DataProcessingApplication(ApplicationProgram):
    """
    Class representing the `DataProcessingApplication` entity, which inherits from:
    - ApplicationProgram

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cbf42aa6_9e11_4be8_932a_ae3c792ab17d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataProcessingApplication'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataProcessingApplication(
    
    class_iri='https://w3id.org/emmo#EMMO_cbf42aa6_9e11_4be8_932a_ae3c792ab17d',
    
    class_name='DataProcessingApplication',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cbf42aa6_9e11_4be8_932a_ae3c792ab17d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataProcessingApplication',
        alias="class_name"
    )
    

    
    

    

    
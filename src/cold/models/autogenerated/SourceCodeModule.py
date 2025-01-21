
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SoftwareModule import Software



from .ProgrammingLanguageModule import ProgrammingLanguage







class SourceCode(Software, ProgrammingLanguage):
    """
    Class representing the `SourceCode` entity, which inherits from:
    - Software, ProgrammingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_348d39f7_6a17_49d1_9860_9b33b69b51de'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SourceCode'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SourceCode(
    
    class_iri='https://w3id.org/emmo#EMMO_348d39f7_6a17_49d1_9860_9b33b69b51de',
    
    class_name='SourceCode',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_348d39f7_6a17_49d1_9860_9b33b69b51de',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SourceCode',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IconModule import Icon







class BPMNDiagram(Icon):
    """
    Class representing the `BPMNDiagram` entity, which inherits from:
    - Icon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#BPMNDiagram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BPMNDiagram'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BPMNDiagram(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#BPMNDiagram',
    
    class_name='BPMNDiagram',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#BPMNDiagram',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BPMNDiagram',
        alias="class_name"
    )
    

    
    

    

    
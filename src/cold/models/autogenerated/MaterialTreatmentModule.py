
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialsProcessingModule import MaterialsProcessing



from .ManufacturingModule import Manufacturing







class MaterialTreatment(MaterialsProcessing, Manufacturing):
    """
    Class representing the `MaterialTreatment` entity, which inherits from:
    - MaterialsProcessing, Manufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fc859d37_408d_44b6_b345_a0ea0b65121e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialTreatment'`
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
    obj = MaterialTreatment(
    
    class_iri='https://w3id.org/emmo#EMMO_fc859d37_408d_44b6_b345_a0ea0b65121e',
    
    class_name='MaterialTreatment',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fc859d37_408d_44b6_b345_a0ea0b65121e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialTreatment',
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
    

    
    

    

    
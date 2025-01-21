
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel







class EMMO(LinkedDataModel):
    """
    Class representing the `EMMO` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_802d3e92_8770_4f98_a289_ccaaab7fdddf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EMMO'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `hasPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `extra_property` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `extraProperty`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EMMO(
    
    class_iri='https://w3id.org/emmo#EMMO_802d3e92_8770_4f98_a289_ccaaab7fdddf',
    
    class_name='EMMO',
    
    definition="example_value",
    
    conceptualisation="example_value",
    
    hasPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    extra_property=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_802d3e92_8770_4f98_a289_ccaaab7fdddf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EMMO',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    hasPart: Optional[str] = Field(
        None,
        alias="hasPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    extra_property: Optional[str] = Field(
        None,
        alias="extraProperty"
    )
    

    
    

    
    
    
def custom_method(self):
    return f"Custom method in {self.__class__.__name__}"

    
    

    